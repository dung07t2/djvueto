<template>
  <v-layout align-center
            justify-center>
    <v-flex xs12
            sm10
            md8
            lg6
            xl6>
      <h3>Login</h3>
      <login-form :redirect="{ name: 'index' }" />
      <br>
      <p>You don't have an account?
        <nuxt-link :to="{ name: 'auth-registration' }">Register!</nuxt-link>
      </p>
      <br>
      <p>Forgot password?
        <nuxt-link :to="{ name: 'auth-password-reset' }">Reset!</nuxt-link>
      </p>
    </v-flex>
  </v-layout>
</template>

<script>
import LoginForm from '~/components/auth/LoginForm.vue'

export default {
  name: 'auth-login',
  middleware: 'no-auth',
  components: { LoginForm },
}
</script>
