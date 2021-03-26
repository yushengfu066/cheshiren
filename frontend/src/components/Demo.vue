<template>
  <v-app>
    <router-view></router-view>
  </v-app>
</template>

<script>
import HelloWorld from '@/components/HelloWorld';

export default {
  name: 'Demo',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
