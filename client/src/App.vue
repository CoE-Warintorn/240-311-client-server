<template>
  <div id="app">
    <div>
      <b-navbar type="dark" variant="dark">
        <b-container fluid="">
          <b-navbar-brand style="padding-left: 2%">Book Library</b-navbar-brand>
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="ml-auto">
              <b-button variant="outline-light">github</b-button>
              <b-nav-item>5910110044</b-nav-item>
            </b-navbar-nav>
          </b-collapse>  
        </b-container>
        
      </b-navbar>
    </div>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
    </div> -->
    <div>
      <b-row style="margin-top: 2%">
        <b-col>
          <router-view/>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  text-align: center;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
