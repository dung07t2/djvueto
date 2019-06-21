<template>
  <v-layout justify-center
            align-center>
    <v-flex xs12
            sm10
            md8
            lg6
            xl6>
      <h3>Change password</h3>
      <password-change-form :redirect="{ name: 'auth-info' }"
                            @success="successChange" />
      <br>
      <p>Forgot password?
        <nuxt-link :to="{ name: 'auth-password-reset' }">Reset!</nuxt-link>
      </p>
    </v-flex>
  </v-layout>
</template>

<script>
import PasswordChangeForm from '~/components/auth/PasswordChangeForm.vue';

export default {
  name: 'auth-password-change',
  middleware: 'auth',
  // data: () => ({
  // }),
  methods: {
    successChange() {
      global.console.log('successChange');
    }
  },
  components: { PasswordChangeForm }
}
</script>
