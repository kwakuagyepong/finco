<script context="module">
  export async function load({ url }) {
    return { url: url.pathname };
  }
</script>

<script>
  import Header from "$lib/Header.svelte";
  import "./styles/global.css";

  export let url;
</script>

{#if url !== "/"}
  <Header title="Finco Ops" />
{/if}

<slot />
