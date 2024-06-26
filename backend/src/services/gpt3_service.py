import openai
import json
from services.azure_blob_service import save_violations_to_azure
from services.user_service import update_user_violations_to_azure
from azure.storage.blob import BlobServiceClient

def load_rules_from_azure(storage_connection_string: str, container_name: str):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    blob_client = container_client.get_blob_client("rules.json")
    rules_str = blob_client.download_blob().readall().decode('utf-8')
    
    rules_json = json.loads(rules_str)
    return rules_json["rules"]

def check_prompt_against_rules(prompt, rules):
    violations = []
    
    for rule_data in rules:
        # Use ChatGPT to check the rule against the prompt
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=f"Check if the following prompt violates the rule: {rule_data['rule']} \nPrompt: {prompt} \nRespond only with '1' (violation) or '0' (no violation). Do not add any unnecessary text.",
            max_tokens=10  # Limit the output to '1' or '0'
        )
        
        # Extract the binary response
        binary_response = response.choices[0].text.strip()
        
        if '1' in binary_response:
            violations.append({"document": rule_data["document"], "rule": rule_data["rule"]})
    
    return violations

def generate_responses(prompt: str, username: str, model_name: str, storage_connection_string: str, container_name: str):
    rules = load_rules_from_azure(storage_connection_string, container_name)
    violations = check_prompt_against_rules(prompt, rules)
    
    if len(violations)>0:
        # Save violations to Azure Blob
        save_violations_to_azure(storage_connection_string, container_name, prompt, violations)

        # Update user violations count
        update_user_violations_to_azure(storage_connection_string, container_name, username, len(violations))

        return {"response": f"This is invalid and goes against organization's guidelines. Please feel free to talk about anything else."}
    
    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return {"response": completion.choices[0].message}
