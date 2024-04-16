import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import CrudTable from "../Components/CrudTable";

const Rules = () => {
  const [rules, setRules] = useState([""]);
  const [newRule, setNewRule] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch rules data from backend API
    // Replace the fetch call with your actual API call
    fetch("your-backend-url/rules")
      .then((response) => response.json())
      .then((data) => setRules(data))
      .catch((error) => console.error("Error fetching rules:", error));
  }, []);

  const addRule = () => {
    // Add new rule to backend
    // Replace the fetch call with your actual API call
    fetch("your-backend-url/rules", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ rule: newRule }),
    })
      .then((response) => response.json())
      .then((data) => {
        setRules([...rules, data]); // Update rules state with the new rule
        setNewRule(""); // Clear input field
      })
      .catch((error) => console.error("Error adding rule:", error));
  };

  const deleteRule = (id) => {
    // Delete rule from backend
    // Replace the fetch call with your actual API call
    fetch(`your-backend-url/rules/${id}`, {
      method: "DELETE",
    })
      .then(() => {
        setRules(rules.filter((rule) => rule.id !== id)); // Update rules state after deletion
      })
      .catch((error) => console.error("Error deleting rule:", error));
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    // You can now upload 'file' to your backend using FormData or other methods
  };
  return (
    <>
      <div className="container mx-auto mt- p-8 bg-slate-950 rounded-lg">
        {/* Upload PDF */}
        <div className="mb-8 text-center bg-slate-950">
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileUpload}
            className="hidden"
            id="fileInput"
          />
          <label
            htmlFor="fileInput"
            className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded cursor-pointer"
          >
            Upload PDF
          </label>
          {selectedFile && <span className="ml-2">{selectedFile.name}</span>}
        </div>

        {/* Rules CRUD */}
        <div className="mb-8">
          <div className="flex justify-center mb-4">
            <input
              type="text"
              id="newRule"
              value={newRule}
              onChange={(e) => setNewRule(e.target.value)}
              placeholder="Add new rule"
              className="border border-gray-400 rounded py-2 px-4 mr-2"
            />
            <button
              onClick={addRule}
              className="bg-green-500 hover:bg-green-700 text-white py-2 px-4 rounded"
            >
              Add
            </button>
          </div>

          <ul>
            {rules.map((rule) => (
              <li key={rule.id} className="flex items-center mb-2">
                <span>{rule.name}</span>
                <button
                  onClick={() => deleteRule(rule.id)}
                  className="ml-2 bg-red-500 hover:bg-red-700 text-white py-1 px-2 rounded"
                >
                  Delete
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <div>
        <CrudTable />
      </div>
    </>
  );
};

export default Rules;
