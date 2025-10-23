const API_URL = "http://127.0.0.1:5000"; // Flask backend

// Add book
document.getElementById("bookForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = document.getElementById("title").value;
  const author = document.getElementById("author").value;

  await fetch(`${API_URL}/add_book`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, author }),
  });

  document.getElementById("bookForm").reset();
  loadBooks();
});

// Fetch and display all books
async function loadBooks() {
  const res = await fetch(`${API_URL}/books`);
  const books = await res.json();

  const tbody = document.querySelector("#bookTable tbody");
  tbody.innerHTML = "";

  books.forEach((book) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${book.id}</td>
      <td>${book.title}</td>
      <td>${book.author}</td>
      <td>${book.status}</td>
      <td>
        <button onclick="deleteBook(${book.id})">🗑️ Delete</button>
        <button onclick="updateStatus(${book.id}, '${book.status}')">🔁 Toggle Status</button>
      </td>
    `;
    tbody.appendChild(row);
  });
}

// Delete a book
async function deleteBook(id) {
  await fetch(`${API_URL}/delete_book/${id}`, { method: "DELETE" });
  loadBooks();
}

// Update book status
async function updateStatus(id, currentStatus) {
  const newStatus = currentStatus === "available" ? "borrowed" : "available";
  await fetch(`${API_URL}/update_status/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: newStatus }),
  });
  loadBooks();
}

loadBooks();
