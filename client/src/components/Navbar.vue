<template>
  <!-- Navbar -->
  <div>
    <nav class="navbar navbar-expand-lg fixed-top">
      <!-- Container wrapper -->
      <div class="container-fluid">
        <!-- Navbar brand -->
        <!-- Toggle button -->
        <button
          class="navbar-toggler"
          type="button"
          data-mdb-toggle="collapse"
          data-mdb-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="fas fa-bars"></i>
        </button>
        <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <!-- Left links -->
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/admin">HOME</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/library">LIBRARY</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">FAVOURITES</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/login">EXIT</a>
            </li>
          </ul>
          <!-- Search form -->
          <a class="navbar-brand"></a>
          <form class="d-flex input-group w-auto">
            <input
              type="search"
              class="form-control"
              placeholder="Type query"
              aria-label="Search"
            />
            <button
              class="btn btn-danger"
              type="button"
              data-mdb-ripple-color="dark"
            >
              Search
            </button>
          </form>
        </div>
        <!-- Collapsible wrapper -->
      </div>
      <!-- Container wrapper -->
    </nav>
    <!-- Navbar -->
  </div>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
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
</style>
