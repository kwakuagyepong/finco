<script>
  export let visible = false;
  export let title = "";

  const closeModal = () => {
    visible = false;
  };
</script>

{#if visible}
  <div class="modal-backdrop" on:click={closeModal}></div>
  <div class="modal">
    <div class="modal-header">
      <h2>{title}</h2>
      <button class="close" on:click={closeModal}>✖</button>
    </div>
    <div class="modal-body">
      <slot></slot>
    </div>
  </div>
{/if}

<style>
  .modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    padding: 2rem;
    border-radius: 8px;
    z-index: 1001;
    width: 500px;
    max-height: 90%;
    overflow-y: auto;
  }
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  .modal-body {
    display: flex;
    flex-direction: column;
  }
  .close {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.5rem;
  }
</style>
