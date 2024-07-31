<script>
  import Header from "$lib/Header.svelte";

  // Mock data for transactions
  const transactions = [
    {
      id: 1,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Pending",
    },
    {
      id: 2,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Debit",
      amount: "GHS 45,000",
      destinationType: "Inbound",
      status: "BM Approved",
    },
    {
      id: 3,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Inbound",
      status: "Approved",
    },
    {
      id: 4,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Cancelled",
    },
    {
      id: 5,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Debit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Approved",
    },
    {
      id: 6,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Pending",
    },
    {
      id: 7,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Pending",
    },
    {
      id: 8,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Debit",
      amount: "GHS 45,000",
      destinationType: "Inbound",
      status: "BM Approved",
    },
    {
      id: 9,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Inbound",
      status: "Approved",
    },
    {
      id: 10,
      origin: "Credit Union Name",
      destination: "Credit Union Name",
      date: "20/07/2024",
      type: "Credit",
      amount: "GHS 45,000",
      destinationType: "Outbound",
      status: "Cancelled",
    },
  ];
</script>

<Header title="Teller Dashboard" />

<main>
  <div class="transactions-page">
    <div class="filter-section">
      <h2>Filter</h2>
      <a href="#" class="clear-filters">Clear all filters</a>
      <div class="filter-group">
        <h3>Transaction Type</h3>
        <button>Deposit</button>
        <button>Withdrawal</button>
      </div>
      <div class="filter-group">
        <h3>Transaction Status</h3>
        <button>Pending</button>
        <button>BM Approved</button>
        <button>Approved</button>
        <button>Cancelled</button>
      </div>
      <div class="filter-group">
        <h3>Transaction Destination</h3>
        <button>Inbound</button>
        <button>Outbound</button>
      </div>
      <div class="filter-group">
        <h3>Threshold</h3>
        <button>Exceeds</button>
        <button>Within</button>
      </div>
    </div>
    <div class="transactions-section">
      <div class="transactions-header">
        <input type="text" placeholder="Search" />
        <select>
          <option>Customer's name</option>
          <option>Credit Union</option>
        </select>
      </div>
      <table>
        <thead>
          <tr>
            <th>Origin</th>
            <th>Destination</th>
            <th>Date</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Destination Type</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {#each transactions as transaction}
            <tr>
              <td>{transaction.origin}</td>
              <td>{transaction.destination}</td>
              <td>{transaction.date}</td>
              <td class={transaction.type.toLowerCase()}>{transaction.type}</td>
              <td>{transaction.amount}</td>
              <td>{transaction.destinationType}</td>
              <td class={transaction.status.toLowerCase().replace(" ", "-")}
                >{transaction.status}</td
              >
            </tr>
          {/each}
        </tbody>
      </table>
      <div class="pagination">
        <button>Prev</button>
        <button>1</button>
        <button>2</button>
        <button>3</button>
        <button>4</button>
        <button>5</button>
        <button>Next</button>
      </div>
    </div>
  </div>
</main>
