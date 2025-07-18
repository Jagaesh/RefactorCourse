const swapi = require('./script-api');

describe('swapi asynchronous testing', () => {
    it('calls swapi to get people', (done) => {
        expect.assertions(1)
        swapi.getPeople(fetch).then(data => {
            expect(data.count).toEqual(87)
            done();
        })
    })

    it('calls swapi to get people with a promise', () => {
        expect.assertions(2)
        return swapi.getPeoplePromise(fetch).then(data => {
            expect(data.count).toEqual(87)
            expect(data.results.length).toBeGreaterThan(5)
        })
    })

    it('calls swapi to get people with a promise async', async () => {
        const data = await swapi.getPeoplePromise(fetch)
        expect(data.count).toEqual(87)
        expect(data.results.length).toBeGreaterThan(5)
    })
})

describe('swapi Mock testing', () => {
    it('getPeople returns count and results', () => {
        const mockFetch = jest.fn()
            .mockReturnValue(Promise.resolve({
                json: () => Promise.resolve({
                    count: 87,
                    results: [0,1,2,3,4,5],
                })
            }))
        
        expect.assertions(2)
        return swapi.getPeoplePromise(mockFetch).then(data => {
            expect(mockFetch.mock.calls.length).toBe(1);
            expect(mockFetch).toHaveBeenCalledWith('https://swapi.py4e.com/api/people');
        })
    })

    it('getPeople returns count and results async', async () => {
        const mockResponse = {
            count: 87,
            results: [0, 1, 2, 3, 4, 5],
        };

        const mockFetch = jest.fn().mockResolvedValue({
            json: jest.fn().mockResolvedValue(mockResponse),
        });

        const data = await swapi.getPeoplePromise(mockFetch);

        expect(mockFetch).toHaveBeenCalledTimes(1);
        expect(mockFetch).toHaveBeenCalledWith('https://swapi.py4e.com/api/people');
        expect(data).toEqual(mockResponse);
        expect(data.count).toEqual(87)
        expect(data.results.length).toBeGreaterThan(5)
    });
})
