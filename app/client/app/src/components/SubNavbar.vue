<template>
  <nav class="tabs is-small">
    <ul>
      <router-link tag="li" activeClass='is-active' :to="{ name: 'riskTypes'}"><a>Risk types</a></router-link>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'SubNavbar'
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
