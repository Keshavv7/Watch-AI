import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Signup = ({ setUserType }) => {
  const [role, setRole] = useState("user"); // State to track selected role
  const Navigate = useNavigate();

  const handleSignup = () => {
    // Logic to handle login based on selected role
    console.log("Role selected:", role);
    console.log("Signup successful!");
    setUserType(role);
    // Add your signup logic here...
    if(role === "user") Navigate("/chatbot"); // Navigate to chatbot page
    else Navigate("/admin"); //
  };

  return (
    <div className="flex items-center justify-center h-screen bg-zinc-200 dark:bg-zinc-800">
      <div className="bg-white dark:bg-zinc-700 p-8 rounded-lg shadow-md w-full max-w-sm">
        <div className="mb-4">
          <h2 className="text-3xl font-bold text-center text-purple-600 dark:text-purple-300">
            SIGN UP
          </h2>
        </div>
        <div className="mb-4">
          <label
            htmlFor="role"
            className="block text-zinc-700 dark:text-zinc-300 text-sm font-bold mb-2"
          >
            I am a:
          </label>
          <select
            id="role"
            className="block appearance-none w-full bg-zinc-200 dark:bg-zinc-600 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-600 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
            value={role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option value="user">User</option>
            <option value="admin">Admin</option>
          </select>
        </div>
        <div className="mb-4">
          <label
            htmlFor="Email"
            className="block text-zinc-700 dark:text-zinc-300 text-sm font-bold mb-2"
          >
            Email
          </label>
          <input
            type="email"
            id="email"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-zinc-700 dark:text-zinc-300 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="email"
            required
          />
        </div>
        <div className="mb-6">
          <label
            htmlFor="password"
            className="block text-zinc-700 dark:text-zinc-300 text-sm font-bold mb-2"
          >
            Password
          </label>
          <input
            type="password"
            id="password"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-zinc-700 dark:text-zinc-300 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="********"
          />
        </div>
        <div className="mb-6">
          <label
            htmlFor="confirmPassword"
            className="block text-zinc-700 dark:text-zinc-300 text-sm font-bold mb-2"
          >
            Confirm Password
          </label>
          <input
            type="password"
            id="confirmPassword"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-zinc-700 dark:text-zinc-300 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="********"
          />
        </div>
        <div className="flex items-center justify-center">
          <button
            className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
            onClick={handleSignup}
          >
            Signup
          </button>
        </div>
        <div className="mt-4 text-center">
          <p className="text-zinc-600 dark:text-zinc-400 text-sm">
            Already have an account?{" "}
            <a
              href="/login"
              className="text-purple-600 dark:text-purple-300 hover:text-purple-800 font-bold"
            >
              Login
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Signup;
