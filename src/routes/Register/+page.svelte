<script>
  import { onMount } from "svelte";

  let currentStep = 1; // Track the current step of the registration process
  let formData = {
    name: "",
    email: "",
    number: "",
    role: "",
    creditUnionName: "",
    creditUnionlocation: "",
    creditUnionPhone: "",
    logo: null,
  };

  function handleNext(event) {
    // Prevent form submission
    event.preventDefault();

    if (currentStep < 3) {
      currentStep += 1; // Move to the next step
    } else {
      // Submit the form data or further process it
      console.log("Submit data", formData);
    }
  }

  function handleBack(event) {
    // Prevent form submission
    event.preventDefault();

    if (currentStep > 1) {
      currentStep -= 1; // Move to the previous step
    }
  }

  // Function to handle file input for logo
  function handleFileChange(event) {
    formData.logo = event.target.files[0];
  }
</script>

<div class="logincontainer">
  <!-- Left Container for Form -->
  <div class="login-container">
    <div class="card">
      <img src="/Finco-ops logo.png" alt="Logo" class="logo" />
      <h2>Register</h2>
      <p>Tell us a bit about your credit union</p>

      <!-- Progress Bar -->
      <div class="progress-bar-container">
        <div class="progress-bar" style="width: {currentStep * 33.3}%"></div>
      </div>

      <form on:submit|preventDefault={handleNext}>
        {#if currentStep === 1}
          <label for="name">Name</label>
          <input
            type="text"
            id="name"
            bind:value={formData.name}
            placeholder="Enter your name"
            required
          />

          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            bind:value={formData.email}
            placeholder="Enter your email"
            required
          />

          <label for="number">Mobile Number</label>
          <input
            type="number"
            id="number"
            bind:value={formData.number}
            placeholder="Your personal mobile number"
            required
          />

          <label for="role">Role</label>
          <input
            type="text"
            id="role"
            bind:value={formData.role}
            placeholder="What is your role at your company?"
            required
          />
        {/if}

        {#if currentStep === 2}
          <label for="creditUnionName">Credit Union Name</label>
          <input
            type="text"
            id="creditUnionName"
            bind:value={formData.creditUnionName}
            placeholder="Enter your credit union's name"
            required
          />

          <label for="creditUnionlocation">Location</label>
          <input
            type="location"
            id="creditUnion"
            bind:value={formData.creditUnionlocation}
            placeholder="Enter credit union's location"
            required
          />
        {/if}

        {#if currentStep === 3}
          <label for="logo">Logo</label>
          <input
            type="file"
            id="logo"
            accept="image/*"
            on:change={handleFileChange}
          />
        {/if}

        <!--Navigation Buttons-->
        <div class="button-container">
          {#if currentStep > 1}
            <button type="button" on:click={handleBack}>Back</button>
          {/if}
          <button type="submit">Next</button>
        </div>
      </form>
      <p>
        Already registered? <a href="login">Log In</a>
      </p>
    </div>
  </div>

  <!-- Right Container for Image -->
  <div class="image-container">
    <img src="finco image.png" alt="Descriptive Alt Text" />
  </div>
</div>

<style>
  /* Additional styles for progress bar */
  .progress-bar-container {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin-bottom: 20px;
  }

  .progress-bar {
    height: 10px;
    background-color: #007bff;
    border-radius: 5px;
    transition: width 0.4s ease;
  }

  /* Existing styles */
  .logincontainer {
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    overflow: hidden;
    align-items: stretch;
    background-color: #ffffff;
  }

  .login-container,
  .image-container {
    flex: 1;
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
    width: 90%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }

  .button-container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }

  button {
    flex: 1;
    margin: 0 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    padding: 10px;
    border-radius: 5px;
    border: none;
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
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
