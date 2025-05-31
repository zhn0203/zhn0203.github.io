import React, { useState } from 'react';

export default function Home() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const res = await fetch('/api/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    setResults(data);
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">SmartSearch Presenter</h1>
      <input
        className="border p-2 w-full mb-4"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter a topic..."
      />
      <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={handleSearch}>Search</button>
      <div className="mt-6">
        {results.map((item, idx) => (
          <div key={idx} className="border rounded p-4 mb-2">
            <h2 className="font-semibold">{item.title}</h2>
            <p>{item.snippet}</p>
            <a href={item.link} className="text-blue-600 underline">View</a>
          </div>
        ))}
      </div>
    </div>
  );
}
