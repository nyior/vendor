const is_authenticated = JSON.parse(
  window.localStorage.getItem("authenticated")
);

const user_id = JSON.parse(window.localStorage.getItem("user_id"));

export { is_authenticated };

export { user_id };
