<template>
     <yandex-map :coords="coords">
    </yandex-map>
</template>

<script>
import { yandexMap, ymapMarker } from '../../../src'
export default {
    components: { yandexMap, ymapMarker }
}
</script>

<style>
ymap-container {
  height: 600px;
}
</style>