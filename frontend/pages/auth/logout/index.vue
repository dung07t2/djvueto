<template>
  <v-layout align-center
            justify-center
            column>
    <h4>Are you sure you want to quit?</h4>
    <logout-form :redirect="{ name: 'index' }" />
  </v-layout>
</template>

<script>
import LogoutForm from '~/components/auth/LogoutForm.vue'

export default {
  name: 'auth-logout',
  components: { LogoutForm }
}
</script>
