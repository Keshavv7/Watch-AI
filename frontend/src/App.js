import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Pages/Login";
import Signup from "./Pages/Signup";
import Chatbot from "./Pages/Chatbot/Chatbot";
import Admin from "./Pages/Admin/Admin";
import Navbar from "./Components/Navbar/Navbar";
import Contact from "./Pages/Contact";
import Rules from "./Pages/Rules";

const App = () => {
  const [userType, setUserType] = useState("");

  return (
    <Router>
      <div>
        {/* {userType === "admin" && */}
        <Navbar />
        {/* }  */}

        <Routes>
          <Route path="/login" element={<Login setUserType={setUserType} />} />

          <Route
            path="/signup"
            element={<Signup setUserType={setUserType} />}
          />

          {/* {userType === "admin" && ( */}
          <Route path="/contact-us" element={<Contact />} />
          {/* )} */}

          {/* {userType === "admin" && ( */}
          <Route path="/rules" element={<Rules />} />
          {/* )} */}

          {/* {userType === "user" && ( */}
          <Route path="/chatbot" element={<Chatbot />} />
          {/* )} */}

          {/* {userType === "admin" &&  */}
          <Route path="/admin" element={<Admin />} />
          {/* } */}

          {/* {(!userType || (userType !== "user" && userType !== "admin")) && (
            <Route path="*" element={<Login setUserType={setUserType} />}  />
          )} */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
