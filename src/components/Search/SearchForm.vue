<template>
    <!-- <form
      class="form-group has-search my-0 ml-auto mr-auto"
      @submit.prevent="onSubmit"
    >
        <input
          class="form-control mr-sm-2 p-3 px-4"
          type="search"
          placeholder="Search for products/services"
          required
          v-model="searchWord"
        /> 
        <span class="fa fa-search form-control-feedback"></span>
    </form> -->

    <form 
        class="input-group ml-auto mr-auto"
        @submit.prevent="onSubmit"
    >
       <input 
            class="form-control py-2 border-right-0 border" 
            type="search" 
            placeholder="search for things and people"
            v-model="searchWord"
        >
        <span class="input-group-append">
            <div class="input-group-text bg-white">
                <i 
                    class="fa fa-search" 
                    aria-hidden="true"
                    @click="onSubmit"
                >

                </i>
            </div>
        </span>
    </form>

</template>

<script>

export default {
  name: "search",

  data() {
    return {
      searchWord: null,
      isAuth: null
    };
  },

  methods: {
    onSubmit() {
      this.$router.push({
        name: "search",
        params: { search_key: this.searchWord }
      });
    }
  }
};
</script>

<style scoped>

    form {
        width: 50rem;
        height: 3rem;
        border-radius: 10px;
    }

    .input-group-text{
        border: none;
        font-size: 1.6rem;
        color:  #7a09c4;
    }

    @media only screen and (max-width: 600px) {
        form {
        width:  100%;
        height: 3rem;
        border-radius: 10px;
        }

        .input-group-text{
            border: none;
            font-size: 1.4rem;
            color:  #7a09c4;
        }
    }  

</style>
