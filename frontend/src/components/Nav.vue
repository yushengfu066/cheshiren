<template>
  <div>
    <v-list>
      <v-list-item>
        <v-list-item-avatar>
          <v-img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_r2.png"></v-img>
        </v-list-item-avatar>
      </v-list-item>

      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title class="title">
            topredito放款还款平台
          </v-list-item-title>
          <v-list-item-subtitle>topredito</v-list-item-subtitle>
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
name: "Nav",
  data: () => ({
    selectedItem: 0,
    items: [
      { text: '首页', icon: 'mdi-upload', to: '/dashboard/home' },
      { text: '放款管理', icon: 'mdi-folder', to: '/dashboard/case' },
      { text: '还款管理', icon: 'mdi-account-multiple', to: '/dashboard/paytask' },
      // { text: '测试报告', icon: 'mdi-star', to: '/login' },
      // { text: 'Recent', icon: 'mdi-history' },
      // { text: 'Offline', icon: 'mdi-check-circle' },
      // { text: 'Uploads', icon: 'mdi-upload' },
      // { text: 'Backups', icon: 'mdi-cloud-upload' },
    ],
  }),
}
</script>

<style scoped>

</style>