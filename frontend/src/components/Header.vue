<template>
<header class="">
  <nav class="navbar navbar-expand-lg shadow-md py-2 bg-dark-gray relative flex items-center w-full justify-between">
    <div class="px-6 w-full flex flex-wrap items-center justify-between">
      <div class="flex items-center">
        <button
          class="navbar-toggler border-0 py-3 lg:hidden leading-none text-xl bg-transparent text-gray-600 hover:text-gray-700 focus:text-gray-700 transition-shadow duration-150 ease-in-out mr-2"
          type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContentY"
          aria-controls="navbarSupportedContentY" aria-expanded="false" aria-label="Toggle navigation">
          <svg aria-hidden="true" focusable="false" data-prefix="fas" class="w-5" role="img"
            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
            <path fill="currentColor"
              d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z">
            </path>
          </svg>
        </button>
      </div>
      <div class="navbar-collapse collapse grow items-center" id="navbarSupportedContentY">
        <ul class="navbar-nav mr-auto lg:flex lg:flex-row mt-2">
          <li class="nav-item">
            <a class="nav-link block pr-2 lg:px-2 py-2 text-gray-100 hover:text-gray-400 focus:text-gray-400 transition duration-150 ease-in-out underline-one font-rale"
              href="#/" data-mdb-ripple="true" data-mdb-ripple-color="light">Главная</a>
          </li>
          <li class="nav-item">
            <a class="nav-link block pr-2 lg:px-2 py-2 text-gray-100 hover:text-gray-400 focus:text-gray-400 transition duration-150 ease-in-out underline-one font-rale"
              href="#/Chart/" data-mdb-ripple="true" data-mdb-ripple-color="light">Графики</a>
          </li>
          <li class="nav-item">
            <a class="nav-link block pr-2 lg:px-2 py-2 text-gray-100 hover:text-gray-400 focus:text-gray-400 transition duration-150 ease-in-out underline-one font-rale"
              href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">Pricing</a>
          </li>
          <li class="nav-item mb-2 lg:mb-0">
            <a class="nav-link block pr-2 lg:px-2 py-2 text-gray-100 hover:text-gray-400 focus:text-gray-400 transition duration-150 ease-in-out underline-one font-rale"
              href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">About</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- Navbar -->
</header>
</template>

<script>
export default {

}
</script>

<style>
.underline-one {
	color: #f3f4f6; /* Цвет обычной ссылки */
    position: relative;
    cursor: pointer;
    text-decoration: none; /* Убираем подчеркивание */
}
.underline-one:after {
	content: "";
    display: block;
    position: absolute;
    right: 0;
    bottom: 3px;
    width: 0;
    height: 2px; /* Высота линии */
    background-color: rgb(255, 255, 255); /* Цвет подчеркивания при исчезании линии*/
    transition: width 0.5s; /* Время эффекта */
}

.underline-one:hover:after {
	content: "";
    width: 95%;
    display: block;
    position: absolute;
    left: 0;
    bottom: 3px;
    height: 2px; /* Высота линии */
    background-color: rgb(0, 255, 255); /* Цвет подчеркивания при появлении линии*/
    transition: width 0.5s;  /* Время эффекта */
}
</style>