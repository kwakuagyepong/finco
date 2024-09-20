<script>
  import Header from "$lib/Header.svelte";
  import { writable } from "svelte/store";

  let isActive = true;
  // @ts-ignore
  let selectedRegions = [];
  const regions = [
    "Greater Accra",
    "Bono East",
    "Eastern",
    "Ahafo",
    "Ashanti",
    "Bono",
    "Central",
    "Northern",
    "Volta",
    "Savannah",
    "Oti",
    "North East",
    "Western North",
    "Upper West",
    "Western",
    "Upper East",
  ];

  const creditUnions = [
    {
      id: 1,
      name: "Credit Union Name",
      branches: "Kasoa",
      accountNumber: "123456789",
      managerName: "Tom Hardy",
      status: "Active",
    },
    {
      id: 2,
      name: "Credit Union Name",
      branches: "Kasoa",
      accountNumber: "123456789",
      managerName: "Tom Hardy",
      status: "Active",
    },
    // Additional entries...
    {
      id: 10,
      name: "Credit Union Name",
      branches: "Kasoa",
      accountNumber: "123456789",
      managerName: "Tom Hardy",
      status: "Inactive",
    },
  ];

  const selectedCreditUnion = writable(null);

  // @ts-ignore
  const selectCreditUnion = (creditUnion) => {
    selectedCreditUnion.set(creditUnion);
  };

  function applyFilters() {
    console.log("Status:", isActive ? "Active" : "Inactive");
    // @ts-ignore
    console.log("Selected Regions:", selectedRegions);
  }

  function clearAll() {
    isActive = true;
    selectedRegions = [];
  }
</script>

<Header title="Teller Dashboard" />

<main>
  <div class="filter-container">
    <h2>Filter</h2>
    <div>
      <h4>Status</h4>
      <label>
        <input type="radio" bind:group={isActive} value={true} /> Active
      </label>
      <label>
        <input type="radio" bind:group={isActive} value={false} /> Inactive
      </label>
    </div>
    <div>
      <h4>Regional Location</h4>
      <div class="region-grid">
        {#each regions as region}
          <label>
            <input
              type="checkbox"
              bind:group={selectedRegions}
              value={region}
            />
            {region}
          </label>
        {/each}
      </div>
    </div>
    <button on:click={clearAll}>Clear All Filters</button>
    <button on:click={applyFilters}>Apply Filters</button>
  </div>

  <div class="account-section">
    <div class="account-header">
      <input type="text" placeholder="Search" />
      <select>
        <option>Credit Union Name</option>
        <option>Customer's Name</option>
      </select>
    </div>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Branches</th>
          <th>Account Number</th>
          <th>Manager Name</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {#each creditUnions as creditUnion}
          <tr on:click={() => selectCreditUnion(creditUnion)}>
            <td>{creditUnion.name}</td>
            <td>{creditUnion.branches}</td>
            <td>{creditUnion.accountNumber}</td>
            <td>{creditUnion.managerName}</td>
            <td class={creditUnion.status.toLowerCase().replace(" ", "-")}
              >{creditUnion.status}</td
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
  {#if $selectedCreditUnion}
    <div class="account-details">
      <h3>Account Details</h3>
      <p><strong>Name:</strong> {$selectedCreditUnion.name}</p>
      <p><strong>Branches:</strong> {$selectedCreditUnion.branches}</p>
      <p>
        <strong>Account Number:</strong>
        {$selectedCreditUnion.accountNumber}
      </p>
      <p><strong>Manager Name:</strong> {$selectedCreditUnion.managerName}</p>
      <p><strong>Status:</strong> {$selectedCreditUnion.status}</p>
    </div>
  {/if}
</main>

<style>
  main {
    display: grid;
    grid-template-columns: 1fr 3fr 2fr;
    gap: 20px;
    padding: 20px;
  }

  .filter-container {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
    height: max-content;
  }

  .account-section {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .account-details {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    display: none; /* Initially hidden */
  }

  .account-details.active {
    display: block; /* Show when an account is selected */
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th,
  td {
    padding: 8px;
    border: 1px solid #ccc;
  }

  input[type="text"],
  select {
    padding: 8px;
    margin: 10px 0;
    display: block;
    width: 100%;
  }

  .pagination {
    padding: 10px 0;
    text-align: center;
  }

  button {
    padding: 8px 16px;
    margin-right: 10px;
    background-color: blue;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .region-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
</style>
