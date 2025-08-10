// static/app.js
$(function() {
  function fetch() {
    const sport = $("#sport").val();
    const level = $("#level").val();
    let url = "/api/tournaments";
    let params = [];
    if (sport) params.push("sport=" + encodeURIComponent(sport));
    if (level) params.push("level=" + encodeURIComponent(level));
    if (params.length) url += "?" + params.join("&");
    $("#results").html("<em>Loading...</em>");
    $.getJSON(url, function(data) {
      if (!data.results || !data.results.length) {
        $("#results").html("<em>No tournaments found</em>");
        return;
      }
      let html = "";
      data.results.forEach(function(t) {
        html += `<div class="card">
          <img class="thumb" src="${t.image_url || 'https://via.placeholder.com/160x100?text=No+Image'}" alt="thumb" />
          <div class="meta">
            <div><span class="sport">${t.sport}</span> — <strong>${t.name}</strong></div>
            <div class="small">${t.level} | ${t.start_date} → ${t.end_date}</div>
            <div style="margin-top:6px">${t.summary}</div>
            <div style="margin-top:8px" class="small">
              <a href="${t.official_url}" target="_blank">Official</a> |
              ${t.streaming_links && t.streaming_links.length ? t.streaming_links.map(l => `<a href="${l}" target="_blank">Watch</a>`).join(" | ") : "No stream info"}
            </div>
          </div>
        </div>`;
      });
      $("#results").html(html);
    }).fail(function() {
      $("#results").html("<em>Failed to load data. Make sure the server is running.</em>");
    });
  }

  $("#filterBtn").on("click", fetch);
  // initial fetch
  fetch();
}); 