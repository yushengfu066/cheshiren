<template>

  <div>
    <v-list>
      <v-list-item>
        <v-list-item-avatar>
          <v-img src="https://www.testing-studio.com/wp-content/uploads/2019/02/cropped-1024-3-192x192.png"></v-img>
        </v-list-item-avatar>
      </v-list-item>

      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title class="title">
            学员演练测试平台
          </v-list-item-title>
          <v-list-item-subtitle>霍格沃兹测试学院</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <v-list
        nav
        dense
    >
      <v-list-item-group
          v-model="selectedItem"
          color="primary"
      >
        <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="item.to"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
export default {
  data: () => ({
    selectedItem: 0,
    items: [
      { text: '测试用例', icon: 'mdi-folder', to: '/dashboard/testcase' },
      { text: '任务管理', icon: 'mdi-account-multiple', to: '/task' },
      { text: '测试报告', icon: 'mdi-star', to: '/login' },
      { text: 'Recent', icon: 'mdi-history' },
      { text: 'Offline', icon: 'mdi-check-circle' },
      { text: 'Uploads', icon: 'mdi-upload' },
      { text: 'Backups', icon: 'mdi-cloud-upload' },
    ],
  }),
}
</script>

<script>
export default {
name: "Nav"
}
</script>

<style scoped>

</style>