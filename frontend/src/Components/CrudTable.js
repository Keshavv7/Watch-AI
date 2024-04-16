import React from "react";
import "./CrudTable.css";

const CrudTable = () => {
  return (
    <div className="container">
      <div className="table-wrapper">
        <div className="table-title">
          <h2>
            Rule <b>Managing</b>
          </h2>
          <div className="btn-group">
            <a
              href="#addEmployeeModal"
              className="btn btn-success"
              data-toggle="modal"
            >
              <i className="material-icons">&#xE147;</i>{" "}
              <span>Add New Employee</span>
            </a>
            <a
              href="#deleteEmployeeModal"
              className="btn btn-danger"
              data-toggle="modal"
            >
              <i className="material-icons">&#xE15C;</i> <span>Delete</span>
            </a>
          </div>
        </div>
        <div className="table">
          <div className="table-header">
            <div>Name</div>
            <div>Email</div>
            <div>Address</div>
            <div>Phone</div>
            <div>Actions</div>
          </div>
          <div className="table-body">
            <div className="table-row">
              <div>Thomas Hardy</div>
              <div>thomashardy@mail.com</div>
              <div>89 Chiaroscuro Rd, Portland, USA</div>
              <div>(171) 555-2222</div>
              <div>
                <a
                  href="#editEmployeeModal"
                  className="edit"
                  data-toggle="modal"
                >
                  <i
                    className="material-icons"
                    data-toggle="tooltip"
                    title="Edit"
                  >
                    &#xE254;
                  </i>
                </a>
                <a
                  href="#deleteEmployeeModal"
                  className="delete"
                  data-toggle="modal"
                >
                  <i
                    className="material-icons"
                    data-toggle="tooltip"
                    title="Delete"
                  >
                    &#xE872;
                  </i>
                </a>
              </div>
            </div>
            {/* Other table rows go here */}
          </div>
        </div>
        <div className="pagination">{/* Pagination links go here */}</div>
      </div>
      {/* Modals go here */}
    </div>
  );
};

export default CrudTable;
