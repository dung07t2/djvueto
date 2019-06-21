<template>
<v-parallax
    dark
    src="/images/banner.jpg"
  >
  <v-layout column
            justify-center
            align-center>
    <v-flex xs12
            sm6
            offset-sm3>
      <v-card>
        <!-- <v-img
          class="white--text"
          height="50px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        ></v-img> -->
        <v-card-title class="headline">DJVUETO Framework</v-card-title>
        <v-card-text>
          <p>Nuxt.jsx + django rest framework + tensorflow</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn primary
                 flat
                 nuxt
                 to="settings">Settings</v-btn>
          <v-btn primary
                 flat
                 nuxt
                 to="settings">Add recipes</v-btn>
        </v-card-actions>
      </v-card>
      <hr class="my-3">
      <blockquote>
        &#8220;First, solve the problem. Then, write the code.&#8221;
        <footer>
          <small>
            <em>&mdash;my goal</em>
          </small>
        </footer>
      </blockquote>
    </v-flex>
  </v-layout>
</v-parallax>
</template>
