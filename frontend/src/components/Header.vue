<template>
  <header>
    <nav class="border-b border-red-700 ">
      <div class="flex justify-between items-center sm:px-4 sm:py-3 py-2 px-2">
        <div class="sm:ml-10 ml-3 flex flex-row gap-2.5 font-mono items-center justify-center text-whitesmoke">
          <a class="hover:text-yellow-500 font-mono"
            ><svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 18v-5.25m0 0a6.01 6.01 0 001.5-.189m-1.5.189a6.01 6.01 0 01-1.5-.189m3.75 7.478a12.06 12.06 0 01-4.5 0m3.75 2.383a14.406 14.406 0 01-3 0M14.25 18v-.192c0-.983.658-1.823 1.508-2.316a7.5 7.5 0 10-7.517 0c.85.493 1.509 1.333 1.509 2.316V18"
              />
            </svg>
          </a>
          <a class="sm:text-2xl text-lg font-rale hover:text-red-500" href=""> TrueSight</a>
        </div>
        <div class="sm:mr-10 sm:text-xl text-base mr-2">
          <ul class="flex flex-row sm:space-x-8 space-x-2">
            <li>
              <a
                href="#"
                class="text-red-500 font-monster hover:text-red-700"
                >Главная</a
              >
            </li>
            <li>
              <a
                href="#"
                class="text-whitesmoke font-monster hover:text-gray-400 "
                >База данных</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {};
</script>
