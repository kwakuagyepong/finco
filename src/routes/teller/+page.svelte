<script>
  import Header from "$lib/Header.svelte";

  // Mock data for accounts and transactions
  const accounts = [
    {
      name: "Credit Union Name",
      number: "1234 5789 0111 2131",
      location: "Ridge, Accra",
    },
    {
      name: "Credit Union Name",
      number: "1234 5789 0111 2131",
      location: "Ridge, Accra",
    },
    {
      name: "Credit Union Name",
      number: "1234 5789 0111 2131",
      location: "Ridge, Accra",
    },
  ];

  const approvedWithdrawals = [
    { name: "Hyatt Gbekley Josef", amount: "GHS 45,000.00" },
    { name: "Brandon Botosh", amount: "GHS 8,160.00" },
    { name: "Kianna Calzoni", amount: "GHS 2,428.00" },
    { name: "Erin Lubin", amount: "GHS 4,657.00" },
    { name: "Abram Curtis", amount: "GHS 8,981.00" },
    { name: "Lincoln Westervelt", amount: "GHS 9,037.00" },
    { name: "Ryan Rosser", amount: "GHS 4,730.00" },
  ];

  const pendingWithdrawals = [
    { name: "Erin Lubin", amount: "GHS 4,657.00" },
    { name: "Abram Curtis", amount: "GHS 8,981.00" },
    { name: "Lincoln Westervelt", amount: "GHS 9,037.00" },
    { name: "Ryan Rosser", amount: "GHS 4,730.00" },
    { name: "Ashlynn Levin", amount: "GHS 5,476.00" },
    { name: "Jaxson Rhiel Madsen", amount: "GHS 8,626.00" },
    { name: "Marley Herwitz", amount: "GHS 1,183.00" },
  ];

  const transactions = [
    {
      type: "Credit",
      amount: "GHS 45,000.00",
      name: "Credit Union Name",
      date: "Jul 16, 2024 at 9:34",
    },
    {
      type: "Debit",
      amount: "GHS 45,000.00",
      name: "Credit Union Name",
      date: "Jul 16, 2024 at 9:34",
    },
    {
      type: "Debit",
      amount: "GHS 45,000.00",
      name: "Credit Union Name",
      date: "Jul 16, 2024 at 9:34",
    },
    {
      type: "Credit",
      amount: "GHS 45,000.00",
      name: "Credit Union Name",
      date: "Jul 16, 2024 at 9:34",
    },
    {
      type: "Debit",
      amount: "GHS 45,000.00",
      name: "Credit Union Name",
      date: "Jul 16, 2024 at 9:34",
    },
  ];
</script>

<Header title="Teller Dashboard" />

<main>
  <div class="overview">
    <div class="left-section">
      <div class="accounts-section">
        <div class="section-header">
          <h2>Accounts</h2>
          <a href="#">View all</a>
        </div>
        <div class="accounts">
          {#each accounts as account}
            <div class="account-card">
              <p>{account.name}</p>
              <p>{account.number}</p>
              <p>{account.location}</p>
              <a href="#">Transactions →</a>
            </div>
          {/each}
        </div>
      </div>
      <div class="withdrawals-section">
        <div class="withdrawals-summary">
          <div>
            <h3>Newly approved withdrawals</h3>
            <p>24 Requests</p>
            <p>Totalling GHS 83,906</p>
          </div>
          <div>
            <h3>Withdrawals pending approval</h3>
            <p>231 Requests</p>
            <p>Totalling GHS 733,022</p>
          </div>
        </div>
        <div class="withdrawals-details">
          <div>
            <h4>Newly approved withdrawals</h4>
            <ul>
              {#each approvedWithdrawals as withdrawal}
                <li>
                  <img
                    src="https://via.placeholder.com/40"
                    alt={withdrawal.name}
                  />
                  <div>
                    <p>{withdrawal.name}</p>
                    <p>{withdrawal.amount}</p>
                  </div>
                </li>
              {/each}
            </ul>
          </div>
          <div>
            <h4>Withdrawals pending approval</h4>
            <ul>
              {#each pendingWithdrawals as withdrawal}
                <li>
                  <img
                    src="https://via.placeholder.com/40"
                    alt={withdrawal.name}
                  />
                  <div>
                    <p>{withdrawal.name}</p>
                    <p>{withdrawal.amount}</p>
                  </div>
                </li>
              {/each}
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="transactions-section">
      <div class="section-header">
        <h2>Transactions</h2>
        <a href="#">View all</a>
      </div>
      <div class="transactions-filter">
        <button>All</button>
        <button>Deposits</button>
        <button>Withdrawals</button>
      </div>
      <ul class="transactions-list">
        {#each transactions as transaction}
          <li>
            <img src="https://via.placeholder.com/40" alt={transaction.name} />
            <div>
              <p>{transaction.name}</p>
              <p>{transaction.date}</p>
            </div>
            <p class="transaction-amount {transaction.type.toLowerCase()}">
              {transaction.type}
              {transaction.amount}
            </p>
          </li>
        {/each}
      </ul>
    </div>
  </div>
</main>
