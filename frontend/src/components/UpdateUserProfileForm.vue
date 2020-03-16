<template>
  
    <div class=" p-0 mt-5">
        <form
           @submit.prevent="UpdateUserProfileTrigger"
          class="p-3 was-validated"
          enctype="multipart/form-data"
        >
          <div class="form-group">
            
            <input
              type="text"
              class="form-control"

              placeholder="Userame"
              required
              v-model="form.username"
            />
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group">
            
            <input
              type="number"
              class="form-control "
             
              placeholder="Mobile phone number, preferably WhatsApp"
              v-model="form.phone_number"
            />
            <div class="invalid-feedback">Only figures allowed</div>
          </div>
          
          <div class="form-group">
            
            <input
              type="email"
              class="form-control "
              
              placeholder="Valid AUN mail"
              
              v-model="form.email"
            />
            <div class="invalid-feedback">
              Please fill out this field with a valid AUN mail
            </div>
          </div>

          <div class="form-group">
            
            <input
              type="text"
              class="form-control "
              
              placeholder="Your Residence Hall"
              
              v-model="form.residence_hall"
            />
            <div class="invalid-feedback">
              Please fill out this field with a valid AUN mail
            </div>
          </div>
          
          <div class="form-group">
            
            <textarea
              class="form-control"
             
              rows="5"
              placeholder="something about you"
              v-model="form.bio"
            ></textarea>
          </div>

          <button class="btn btn-lg btn-blue" type="submit">Update Profile</button>
        </form>
    </div>
    
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "update-profile",

  props: {
    user: {
      type:Object,
      required: true
    },

  },

  data() {
    return {
      form: {
        user_id: this.user.id,
        username: this.user.username,
        email: this.user.email,
        phone_number: this.user.phone_number,
        residence_hall: this.user.residence_hall,
        bio: this.user.bio
      }
    };
  },
  
  methods: {
    
   UpdateUserProfileTrigger(){
      this.$emit('update-profile', this.form);
    }
  }

};
</script>

<style scoped>

</style>
