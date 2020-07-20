let development = {
  auth: {
    authority: "https://accounts.google.com",
    client_id:
      "882687986755-hntee4hqd2r2lm0tt7gsiuii6gm3lsda.apps.googleusercontent.com",
    redirect_uri: "http://localhost:8080/Logincallback",
    post_logout_redirect_uri: "http://localhost:8080/Logoutcallback",
    response_type: "id_token token",
    scope: "openid profile email",
    loadUserInfo: true,
    automaticSilentRenew: false
  },
  backend: {
    baseUri: "http://localhost:8888"
  }
};

let production = {
  auth: {
    authority: "https://accounts.google.com",
    client_id:
      "882687986755-hntee4hqd2r2lm0tt7gsiuii6gm3lsda.apps.googleusercontent.com",
    redirect_uri: "http://localhost:8888/Logincallback",
    post_logout_redirect_uri: "http://localhost:8888/Logoutcallback",
    response_type: "id_token token",
    scope: "openid profile email",
    loadUserInfo: true
  },
  backend: {
    baseUri: `${location.protocol}//${location.hostname}`
  }
};

let config = process.env.NODE_ENV === "production" ? production : development;

export default config;
