<template>
  <v-card class="elevation-24">
    <v-card-text>
      <h6 v-if="errors.has('uid') || errors.has('token')"
          class="error--text">Ваша ссылка устарела или неправильная. Сверьте текущую ссылку с ссылкой из письма.</h6>
      <form @keyup.enter="submit">
        <v-text-field v-model="new_password1"
                      v-validate="'required|min:8|max:128'"
                      :error-messages="errors.collect('new_password1')"
                      name="new_password1"
                      label="New Password"
                      hint="Your password can not consist only of numbers."
                      :counter="new_password1.length"
                      min="8"
                      max="128"
                      :append-icon="pw1 ? 'visibility_off' : 'visibility'"
                      :append-icon-cb="() => (pw1 = !pw1)"
                      :type="pw1 ? 'password' : 'text'"
                      required />
        <v-text-field v-model="new_password2"
                      v-validate="'required|confirmed:new_password1'"
                      :error-messages="errors.collect('new_password2')"
                      name="new_password2"
                      label="Confirm new password"
                      hint="Re-enter new password."
                      :append-icon="pw2 ? 'visibility_off' : 'visibility'"
                      :append-icon-cb="() => (pw2 = !pw2)"
                      :type="pw2 ? 'password' : 'text'"
                      required />
        <v-btn @click.native="submit"
               :disabled="errors.any()">Set new password</v-btn>
      </form>
    </v-card-text>
  </v-card>
</template>

<script>
import getProperty from '~/utils/getProperty'; // eslint-disable-line

export default {
  props: {
    uid: {
      type: String,
      required: true
    },
    token: {
      type: String,
      required: true
    }
  },
  data: () => ({
    new_password1: '',
    new_password2: '',
    pw1: true,
    pw2: true
  }),
  methods: {
    resetData() {
      Object.assign(this.$data, this.$options.data());
    },
    async submit() {
      if (!await this.$validator.validateAll()) return;
      const fields = { ...this.$props, ...this.$data };
      try {
        await this.$store.dispatch('auth/passwordResetConfirm', { fields });
        this.$emit('success');
        this.resetData();
      } catch (error) {
        const backendErrors = getProperty(error, 'response.data');
        if (backendErrors) this.showBackendErrors(backendErrors);
      }
    },
    showBackendErrors(obj) {
      this.errors.clear();
      Object.keys(obj).forEach(field => {
        obj[field].forEach(msg => {
          this.errors.add(field, msg);
        })
      });
    }
  },
}
</script>
