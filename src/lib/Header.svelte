<script>
  export let title = "Dashboard";

  const handleWithdraw = () => {
    console.log("Withdraw clicked");
  };
  const handleDeposit = () => {
    console.log("Deposit clicked");
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
</script>

<header>
  <nav class="left">
    <a href="/overview">Overview</a>
    <a href="/transactions">Transactions</a>
    <a href="/accounts">Credit Union Accounts</a>
    <a href="/statements">Statements</a>
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
