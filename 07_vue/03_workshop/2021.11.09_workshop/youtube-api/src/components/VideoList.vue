<template>
  <ul>
    <video-list-item 
      v-for="video in videos" 
      :key="video.id.videoId"
      :video="video"
      @select-video="onSelectVideo"
    >
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
ul{
  list-style: none;
  margin: 0px;
  padding: 0px;

  max-width: 5000px;
  width: 100%;
  }

</style>
