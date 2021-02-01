<template>
  <div class="home px-3">
    <Sell />

    <Hero />

    <WideBlockFeatured />

    <ExperienceBlock />

    <Categories />
  </div>
</template>

<script>
import Sell from "@/components/Others/Sell.vue";
import Categories from "@/components/Home/Categories.vue";
import Hero from "@/components/Home/Hero.vue";
import WideBlockFeatured from "@/components/Home/WideBlockFeatured";
import ExperienceBlock from "@/components/Home/ExperienceBlock";

export default {
  name: "home",

  components: {
    Sell,
    Categories,
    ExperienceBlock,
    WideBlockFeatured,
    Hero
  },

  mounted: function() {
    document.title = "Marche`";
  }
};
</script>

<style scoped>
.home-hero {
  padding-bottom: 15rem;
  overflow-y: hidden;
}

.hero-text {
  margin-top: 15rem;
}

.col-md-3:nth-child(n + 5) {
  margin-top: 3rem;
}

@media only screen and (max-width: 600px) {
  .home-hero {
    padding-bottom: 20rem;
    overflow-y: hidden;
  }
  .col-md-3:nth-child(n + 5) {
    margin-top: 0rem;
  }

  .hero-text {
    margin-top: 15rem;
  }
}
</style>
