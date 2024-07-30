<script>
  let username = "";
  let password = "";

  const handleLogin = () => {
    console.log("Logging in with", { username, password });
  };
</script>

<main>
  <h1>Login</h1>
  <form class="login-form" on:submit|preventDefault={handleLogin}>
    <label>
      Username:
      <input type="text" bind:value={username} />
    </label>
    <label>
      Password:
      <input type="password" bind:value={password} />
    </label>
    <button type="submit">Login</button>
  </form>
</main>
