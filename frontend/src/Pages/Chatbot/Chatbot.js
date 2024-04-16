import React, { useEffect, useState } from "react";
import "./Chatbot.css";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState("");

  useEffect(() => {
    // Fake messages data
    const fakeMessages = [
      "Hi AlgoOracle at your service",
      "please enter the stock you'd like to predict",
      "Please Enter Your Target Price",
      "good.....What is your comfortable level for investment loss (in %)",
      "we are Predicting...",
      "great.. do you want to predict another?",
      "Bye",
      ":)",
    ];

    // Simulate message insertion after a delay
    const simulateMessageInsertion = (index) => {
      setTimeout(() => {
        setMessages((prevMessages) => [...prevMessages, fakeMessages[index]]);
      }, 1000 + Math.random() * 2000);
    };

    // Simulate message flow
    fakeMessages.forEach((message, index) => {
      simulateMessageInsertion(index);
    });
  }, []);

  const handleMessageChange = (event) => {
    setMessageInput(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (messageInput.trim() !== "") {
      setMessages((prevMessages) => [...prevMessages, messageInput]);
      setMessageInput("");
    }
  };

  return (
    <div className="chat">
      <div className="chat-title">
        <h1>AlgoOracle</h1>
        <h2>Predict the Future</h2>
        <figure className="avatar">
          <img
            src="http://algom.x10host.com/chat/img/icon-oracle.gif"
            alt="Oracle"
          />
        </figure>
        <div className="r-nav">
          <ul>
            <li>
              <a>X</a>
            </li>
            <li>
              <a>
                <img
                  src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMjAuMS4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iJiMxMDU3OyYjMTA4MzsmIzEwODY7JiMxMDgxO18xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDY0IDY0IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA2NCA2NDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8bGluZWFyR3JhZGllbnQgaWQ9IlNWR0lEXzFfXzQ0MDQyIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjMxLjk5OTMiIHkxPSI3LjI0OTMiIHgyPSIzMS45OTkzIiB5Mj0iNTcuMjczMiIgc3ByZWFkTWV0aG9kPSJyZWZsZWN0Ij4KCTxzdG9wIG9mZnNldD0iMCIgc3R5bGU9InN0b3AtY29sb3I6IzFBNkRGRiIvPgoJPHN0b3Agb2Zmc2V0PSIxIiBzdHlsZT0ic3RvcC1jb2xvcjojQzgyMkZGIi8+Cgo8L2xpbmVhckdyYWRpZW50Pgo8cGF0aCBzdHlsZT0iZmlsbDp1cmwoI1NWR0lEXzJfXzQ0MDQyKTsiIGQ9Ik0yOS44NjQsMjQuNjQ0YzAuMzU1LDAuMjM0LDAuNzc2LDAuMzU0LDEuMTk5LDAuMzU0YzAuMjk2LDAsMC41OTMtMC4wNTgsMC44NjktMC4xNzcgIGw1LjI4NC0yLjI2OEMzOC4zMTcsMjIuMDgyLDM5LDIxLjEwMywzOSwyMCwzMiYjMTA4MzsmIzEwODY7c0MzMC4xODcsMjEuNzU5LDI5LjA2OCwyNC43ODMsMjkuOTk5MiwzMS4wODdDMjkuNTAzLDMxLjEzMywyOS4wOTIsMzEuOTM5LDI5Ljg2NCwzMS42NzNWMjAuMDA0IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjEiPgoJPHN0b3Agb2Zmc2V0PSIxIiBzdHlsZT0ic3RvcC1jb2xvcjojQjczMjQ0Ii8+Cgk8L2NpcmNsZT4KPC9zdmc+Cg=="
                  width="26px"
                  alt="Button"
                />
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div className="messages">
        <div className="messages-content">
          {messages.map((message, index) => (
            <div key={index} className="message new">
              <figure className="avatar">
                <img
                  src="http://algom.x10host.com/chat/img/icon-oracle.gif"
                  alt="Oracle"  
                />
              </figure>
              <span>{message}</span>
            </div>
          ))}
        </div>
      </div>
      <div className="message-box">
        <form onSubmit={handleSubmit}>
          <textarea
            type="text"
            className="message-input"
            placeholder="Type message..."
            value={messageInput}
            onChange={handleMessageChange}
          />
          <button type="submit" className="message-submit sound-on-click">
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default Chatbot;
