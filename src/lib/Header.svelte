<script>
  import { page } from "$app/stores";
  import { derived } from "svelte/store";
  import Modal from "$lib/Modal.svelte";
  import { writable } from "svelte/store";

  export let title = "Dashboard";

  const handleWithdraw = () => {
    showWithdrawModal.set(true);
  };
  const handleDeposit = () => {
    showDepositModal.set(true);
  };
  const handleNotifications = () => {
    console.log("Notifications clicked");
  };
  const handleSettings = () => {
    console.log("Settings clicked");
  };
  const handleProfile = () => {
    console.log("Profile clicked");
  };

  const currentRoute = derived(page, ($page) => $page.url.pathname);

  const showWithdrawModal = writable(false);
  const showDepositModal = writable(false);
</script>

<header>
  <nav class="left">
    <a href="/teller" class:active={$currentRoute === "/teller"}>Overview</a>
    <a
      href="/teller/transactions"
      class:active={$currentRoute === "/teller/transactions"}>Transactions</a
    >
    <a
      href="/teller/Credit Union Accounts"
      class:active={$currentRoute === "/teller/Credit Union Accounts"}
      >Credit Union Accounts</a
    >
    <a href="/statements" class:active={$currentRoute === "/statements"}
      >Statements</a
    >
  </nav>
  <div class="center">
    <img src="/Finco-ops logo.png" alt="Logo" class="logo" />
  </div>
  <div class="right">
    <button on:click={handleWithdraw}>Withdraw</button>
    <button on:click={handleDeposit}>Deposit</button>
    <span on:click={handleNotifications} class="icon">🔔</span>
    <span on:click={handleSettings} class="icon">⚙️</span>
    <span on:click={handleProfile} class="icon profile">👤</span>
  </div>
</header>

<Modal bind:visible={$showWithdrawModal} title="Withdraw">
  <form>
    <label>First Name</label>
    <input type="text" name="first-name" required />
    <label>Last Name</label>
    <input type="text" name="last-name" required />
    <label>Amount</label>
    <input type="number" name="amount" required />
    <label>Account Number</label>
    <input type="text" name="account-number" required />
    <label>Credit Union</label>
    <input type="text" name="credit-union" required />
    <label>ID Number</label>
    <input type="text" name="id-number" required />
    <label>Upload ID Card</label>
    <input type="file" name="id-card" required />
    <button type="submit">Submit</button>
  </form>
</Modal>

<Modal bind:visible={$showDepositModal} title="Deposit">
  <form>
    <label>First Name</label>
    <input type="text" name="first-name" required />
    <label>Last Name</label>
    <input type="text" name="last-name" required />
    <label>Amount</label>
    <input type="number" name="amount" required />
    <label>Account Number</label>
    <input type="text" name="account-number" required />
    <label>Credit Union</label>
    <input type="text" name="credit-union" required />
    <label>ID Number</label>
    <input type="text" name="id-number" required />
    <label>Upload ID Card</label>
    <input type="file" name="id-card" required />
    <button type="submit">Submit</button>
  </form>
</Modal>
