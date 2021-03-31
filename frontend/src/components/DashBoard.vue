<template>
  <v-app>
    <v-navigation-drawer app>
      <!-- -->
      <Nav/>
    </v-navigation-drawer>

    <v-app-bar app>
      <!-- -->
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>

</template>

<script>
import Nav from "./Nav";
export default {

name: "DashBoard",
  components: {
    Nav,
  },
}
</script>

<style scoped>

</style>