function wordCount(text, topWordCount = 10) {
    //content to lowercase and remove punctuation
    const words = text.toLowerCase().replace(/[^\w\s]/g, '').split(/\s+/);
    
    //count the occurrences of each word
    const wordCount = words.reduce((acc, word) => {
        acc[word] = (acc[word] || 0) + 1;
        return acc;
    }, {});
    
    //sort words by count in descending order
    const sortedWords = Object.entries(wordCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, topWordCount);
    
    //numbers of words and their frequencies
    sortedWords.forEach(([word, count]) => {
        console.log(`${word} : ${count} times`);
    });
}

const text = `Hello my name is Harry and I am trying to make word count function in JavaScript. Now, I will try to run this code and it should count total frequencis of similar words.`;
const topWordCount = 10;

wordCount(text, topWordCount);
