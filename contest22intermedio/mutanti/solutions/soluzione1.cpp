#include <iostream>
#include <queue>
using namespace std;

struct State {
	int steps;
	int down;
	int move;
	bool operator<(const State &b) const {
		if (steps != b.steps) steps > b.steps;
		return down < b.down;
	}
};

vector<vector<int>> moves;
int drones, nMoves, length;
int distance(int a, int b) {
	/*printf("MOVA: ");
	for (auto e : moves[a]) printf("%d ", e);
	printf("\nMOVB: ");
	for (auto e : moves[b]) printf("%d ", e);
	printf("\n");*/
	int endA = moves[a][length - 1];
	for (int st = 0; st <= length; ++st) {
		bool fail = false;
		for (int i = 0; i < length - st; ++i) {
			if (moves[a][st + i] != moves[b][i]) {
				fail = true;
				//printf("Fail at st = %d i = %d\n", st, i);
				break;
			}
		}
		if (!fail) {
			//printf("st = %d\n", st);
			for (int i = length - st; i < length; ++i) {
				if (moves[b][i] <= endA)
					fail = true;
			}
			if (fail) continue;
			return st;
		}
	}
	return -1;
}

void test() {
	cin >> drones >> nMoves >> length;
	//printf("N = %d M = %d k = %d\n", drones, nMoves, length);
	moves.clear();
	moves.push_back(vector<int>(length, -1));
	vector<vector<int>> hMoves;
	hMoves.resize(drones + 1);
	for (int i = 1; i <= nMoves; ++i) {
		vector<int> p;
		for (int j = 0; j < length; ++j) {
			int h;
			cin >> h;
			p.push_back(h);
		}
		//printf("hMoves[%d] = %d\n", p[length - 1], i);
		hMoves[p[length - 1]].push_back(i);
		moves.push_back(move(p));
	}
	priority_queue<State> q;
	vector<bool> seen(nMoves + 1);
	q.push({0, 0, 0});
	while (!q.empty()) {
		State s = q.top();
		q.pop();
		if (seen[s.move]) continue;
		seen[s.move] = true;
		if (s.down == drones) {
			cout << s.steps << endl;
			return;
		}
		for (int m : hMoves[s.down]) {
			if (seen[m]) continue;
			int dist = distance(s.move, m);
			//printf("distance(%d, %d) = %d\n", s.move, m, dist);
			if (dist >= 0) {
				q.push({s.steps + dist, s.down + 1, m});
			}
		}
	}
	cout << "-1" << endl;
}

int main() {
	int t; cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		test();
	}
}
