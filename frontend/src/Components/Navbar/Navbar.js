import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./Navbar.module.css";
// cf menu submenu
const Navbar = () => {
  return (
    <nav className={`navbar navbar-expand-lg ${styles.navb}`}>
      <div className={`${styles.main} container-fluid`}>
        {/* <img
          src="./iitt_logo.png"
          alt="iitt logo"
          className={styles.navbarLogo}
        /> */}
        <div className={styles.container}>
          <ul className={`${styles.menu} ${styles.cf}`}>
            <li>
              <a href="/admin">Home</a>
            </li>
            <li>
              <a href="/rules">Rules</a>
            </li>
            <li>
              <a href="/monitor">Monitor</a>
            </li>
            <li>
              <a href="/contact-us">Contact us</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
