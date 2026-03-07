import json

data = json.loads(open("index.html").read().split("<script type=\"text/babel\">")[1].split("</script>")[0].replace("const { useState, useEffect, Component } = React;", "var React = {};"))
