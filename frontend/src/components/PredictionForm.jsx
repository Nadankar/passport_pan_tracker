import React, { useState } from "react";
import axios from "axios";

const PredictionForm = () => {
  const [formData, setFormData] = useState({
    age: "",
    type: "PAN",
    state: "",
    verification_status: "Pending",
    criminal_record: "No",
    documents: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); // Clear previous errors

    try {
        console.log("Sending Data:", formData);

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("API Response:", data);

        if (data.error) {
            setError(data.error);
        } else {
            setPrediction(data.prediction);
        }
    } catch (error) {
        console.error("Prediction Error:", error);
        setError("Failed to fetch prediction. Check server.");
    }
};


  return (
    <div>
      <h2>Passport & PAN Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="age" placeholder="Age" value={formData.age} onChange={handleChange} required />

        <select name="type" value={formData.type} onChange={handleChange} required>
          <option value="PAN">PAN</option>
          <option value="Passport">Passport</option>
        </select>

        <input type="text" name="state" placeholder="State" value={formData.state} onChange={handleChange} required />

        <select name="verification_status" value={formData.verification_status} onChange={handleChange} required>
          <option value="Pending">Pending</option>
          <option value="Completed">Completed</option>
          <option value="Rejected">Rejected</option>
        </select>

        <select name="criminal_record" value={formData.criminal_record} onChange={handleChange} required>
          <option value="No">No</option>
          <option value="Yes">Yes</option>
        </select>

        <input type="text" name="documents" placeholder="Documents" value={formData.documents} onChange={handleChange} required />

        <button type="submit">Predict</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {prediction !== null && <p>Prediction Result: {prediction}</p>}
    </div>
  );
};

export default PredictionForm;
