<template>
  <div id="app">
    <router-view/>

  </div>
</template>

<style>
#app {
  margin-top: 150px;
}
.navbar {
  width: 100%;
  background-color: #000000;
  overflow: auto;
}

/* Navigation links */
.navbar a {
  float: center;
  padding: 20px;
  color: white;
  text-decoration: none;
  font-size: 18px;
  text-align: center;

}

h1 {
  color: blue;
  margin: -10px;
  padding: 10px;
}

</style>
