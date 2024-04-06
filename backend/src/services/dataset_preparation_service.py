def prepare_dataset(documents):
    dataset = []
    
    for doc_name, text in documents.items():
        interactions = text.split("\n")  # Assuming each line represents a user interaction
        
        for interaction in interactions:
            dataset.append({
                "doc_name": doc_name,
                "interaction": interaction.strip(),
                "label": None  # Placeholder for annotation
            })
    
    return dataset