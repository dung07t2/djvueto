<template>
  <v-layout justify-center
            align-center
            column>
    <template v-if="status === 'success'">
      <h3>Account has been successfully verified.</h3>
      <p>
        Login now
        <router-link :to="{ name: 'auth-login' }">Login</router-link>.
      </p>
    </template>

    <template v-else-if="status === 'fail'">
      <h3>Account was not verified.</h3>
      <p> Verify that the current link matches the link in the email. </p>
      <p> Error: Invalid data. </p>
    </template>
  </v-layout>
</template>

<script>
import { emailVerify } from '~/api/auth'; // eslint-disable-line 

export default {
  name: 'auth-registration-confirm-email',
  middleware: 'no-auth',
  async asyncData({ app, params }) {
    let status;
    try {
      await app.$axios(emailVerify(params));
      status = 'success';
    } catch (error) {
      status = 'fail';
    }
    return { status };
  },
}
</script>
