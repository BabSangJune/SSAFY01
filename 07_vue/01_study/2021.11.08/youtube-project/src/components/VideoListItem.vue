<template>
  <li>
    <img :src="video.snippet.thumbnails.default.url" alt="123">
    {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>

</style>
