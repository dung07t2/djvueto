<template>
  <v-container fluid>
    <v-layout align-center
              justify-center>
      <v-flex xs10>
        <v-card v-if="settings">
          <v-card-text>
            <v-layout row
                      wrap>
              <v-flex xs12>
                <span>Theme</span>
                <v-radio-group v-model="settings.dark"
                               @change="changeSetting">
                  <v-radio label="Dark"
                           :value="true" />
                  <v-radio label="Light"
                           :value="false" />
                </v-radio-group>
              </v-flex>
              <v-flex xs12
                      md6>
                <span>Navigation menu</span>
                <v-switch label="Under the header"
                          v-model="settings.firstDrawerClipped"
                          @change="changeSetting"
                          :disabled="settings.firstDrawerMini"
                          primary />
                <v-switch label="Mini"
                          class="pa-0"
                          v-model="settings.firstDrawerMini"
                          @change="changeSetting"
                          primary />
                <v-switch label="Case"
                          class="pa-0"
                          v-model="settings.firstDrawerRight"
                          @change="changeSetting"
                          primary />
              </v-flex>
              <v-flex xs12
                      md6>
                <span>Chat</span>
                <v-switch label="Case"
                          v-model="settings.secondDrawerRight"
                          @change="changeSetting"
                          primary />
              </v-flex>
              <v-flex xs12
                      md6>
                <span>Healther</span>
                <v-switch label="Fixed"
                          v-model="settings.headerFixed"
                          disabled
                          @change="changeSetting"
                          primary />
              </v-flex>
              <v-flex xs12
                      md6>
                <span>Futer</span>
                <v-switch label="Fixed"
                          v-model="settings.footerFixed"
                          @change="changeSetting"
                          primary />
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'settings',
  data: () => ({
    settings: this.storeSettings,
  }),
  computed: {
    storeSettings() {
      return this.$store.state.settings;
    }
  },
  methods: {
    changeSetting() {
      this.settings.firstDrawerClipped = this.settings.firstDrawerMini || this.settings.firstDrawerClipped;
      this.$store.dispatch('settings/updateSettings', this.settings);
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.settings = { ...this.storeSettings };
    })
  },
}
</script>
