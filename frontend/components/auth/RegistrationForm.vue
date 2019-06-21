<template>
  <v-card class="elevation-24">
    <v-container fluid>
      <form @keyup.enter="submit">
        <v-text-field v-model="username"
                      v-validate="{ rules: {required: true, max: 150, regex: /^[\w.@+-]+$/, unique: 'username'} }"
                      :error-messages="errors.collect('username')"
                      label="Username"
                      name="username"
                      required
                      hint="Only letters, numbers and symbols @ /. / + / - / _."
                      max="150"
                      :counter="150" />
        <v-text-field v-model="email"
                      v-validate="'required|email|unique:email'"
                      :error-messages="errors.collect('email')"
                      label="Email"
                      name="email"
                      type="email"
                      required />
        <v-text-field v-model="password1"
                      v-validate="'required|min:8|max:128'"
                      :error-messages="errors.collect('password1')"
                      name="password1"
                      label="Password"
                      hint="Your password can not consist only of numbers."
                      :counter="password1.length"
                      min="8"
                      max="128"
                      :append-icon="pw1 ? 'visibility_off' : 'visibility'"
                      :append-icon-cb="() => (pw1 = !pw1)"
                      :type="pw1 ? 'password' : 'text'"
                      required />
        <v-text-field v-model="password2"
                      v-validate="'confirmed:password1'"
                      :error-messages="errors.collect('password2')"
                      name="password2"
                      label="Confirm new password"
                      hint="Re-enter new password."
                      :append-icon="pw2 ? 'visibility_off' : 'visibility'"
                      :append-icon-cb="() => (pw2 = !pw2)"
                      :type="pw2 ? 'password' : 'text'"
                      required />
        <v-btn @click.native="submit"
               :disabled="errors.any()">Register</v-btn>
      </form>
    </v-container>
  </v-card>
</template>

<script>
import getProperty from '~/utils/getProperty'; // eslint-disable-line
import { checkExist } from '~/api/auth'; // eslint-disable-line 

export default {
  props: ['redirect'],
  data: () => ({
    username: '',
    email: '',
    firstName: '',
    lastName: '',
    password1: '',
    password2: '',
    pw1: true,
    pw2: true,
  }),
  methods: {
    resetData() {
      Object.assign(this.$data, this.$options.data());
    },
    async submit() {
      const { username, email, password1, password2 } = this.$data;
      try {
        await this.$store.dispatch('auth/registration', { fields: { username, email, password1, password2 } });
        this.$emit('success', email);
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
          if (field === 'non_field_errors') {
            field = 'password2';
          }
          this.errors.add(field, msg);
        })
      });
    }
  },
  created() {
    this.$validator.extend('unique', {
      validate: async (input, field) => {
        const { data } = await this.$axios(checkExist({ [field]: input }));
        return data.valid || { data };
      },
      getMessage: (field, params, { message }) => message
    });
  }
}
</script>
