<script>
  import { browser } from "$app/environment";
  import { goto } from "$app/navigation";
  import { writable } from "svelte/store";

  let email = "";
  let password = "";
  let currentError = null;
  let user = writable(null); // Assuming you want to store user data in a Svelte store

  const login = () => {
    fetch(`https://nkagyepong1.pythonanywhere.com/api/users/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: email, password: password }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("Something not quite right with Server response");
        }
      })
      .then((data) => {
        user.set(data); // Updates the user store with the new data
        goto("/teller"); // Redirects to dashboard after successful login
      })
      .catch((error) => {
        currentError = error.message;
        console.log("Error logging in: ", error);
      });
  };
</script>

<div class="logincontainer">
  <!-- Left Container for Login -->
  <div class="login-container">
    <div class="card">
      <img src="/Finco-ops logo.png" alt="Logo" class="logo" />
      <h2>Log In</h2>
      <p>Welcome back! Please enter your details.</p>
      <form on:submit|preventDefault={login}>
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          bind:value={email}
          placeholder="Enter your email"
          required
        />

        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          bind:value={password}
          placeholder="Enter your password"
          required
        />

        <button type="submit">Login</button>
      </form>
      <p>
        Don't have an account? <a href="Register">Register with us</a>
      </p>
    </div>
  </div>

  <!-- Right Container for Image -->
  <div class="image-container">
    <img src="finco image.png" alt="Descriptive Alt Text" />
  </div>
</div>

<style>
  /* Login page styles */
  .logincontainer {
    display: flex;
    position: fixed; /* Changed from 'relative' to 'fixed' */
    top: 0; /* Set the top to 0 to align with the viewport top */
    left: 0; /* Set the left to 0 to align with the viewport left */
    right: 0; /* Set the right to 0 to align with the viewport right */
    bottom: 0; /* Set the bottom to 0 to align with the viewport bottom */
    overflow: hidden; /* Prevents any content from scrolling */
    align-items: stretch; /* Ensures children stretch to fill the container vertically */
    background-color: #ffffff;
  }

  .login-container,
  .image-container {
    flex: 1; /* Each container takes half the width of the viewport */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .card {
    background: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 90%;
    max-width: 400px;
  }

  input {
    width: 85%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }

  button {
    background-color: #007bff;
    color: white;
    cursor: pointer;
    width: 90%;
  }

  button:hover {
    background-color: #0056b3;
  }

  label {
    display: block;
    margin-bottom: 5px;
  }

  a {
    color: #007bff;
  }

  a:hover {
    text-decoration: underline;
  }

  img {
    width: 100%; /* Ensures the image covers the entire width of its container */
    height: 100%; /* Ensures the image covers the entire height of its container */
    object-fit: cover; /* Adjusts the image size to cover the available space without losing its aspect ratio */
  }
</style>
