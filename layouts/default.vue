<script setup lang="ts">
</script>

useHead ( input: {


    script: [
        {src: 'https://telegram.org/js/telegram-web-app.js', defer: true}
    ],
})

<template>
<div>
<ClientOnly>
<slot/>
</ClientOnly>
</div>

</template>

<style>

</style>