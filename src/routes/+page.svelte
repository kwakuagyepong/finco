<script>
  import { goto } from "$app/navigation";
</script>

<main>
  <h1>Welcome to Finco Ops</h1>
  <button on:click={() => goto("/login")}>Login</button>
  <button on:click={() => goto("/teller")}>Teller Dashboard</button>
  <button on:click={() => goto("/manager")}>Manager Dashboard</button>
  <button on:click={() => goto("/second-manager")}
    >Second Manager Dashboard</button
  >
  <button on:click={() => goto("/super-admin")}>Super Admin Dashboard</button>
</main>

<style>
  main {
    text-align: center;
    padding: 2rem;
  }
  button {
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
  }
  button:hover {
    background-color: #0056b3;
  }
</style>
