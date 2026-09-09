from client import LSMTreeCompactor

def main():
    print("=== LSM-Tree SSTable Compaction Engine ===")
    compactor = LSMTreeCompactor()

    # Older SSTable Level 0
    sst_old = [("alpha", "v1"), ("beta", "v1"), ("gamma", "v1")]
    # Newer SSTable Level 0
    sst_new = [("beta", "v2_updated"), ("gamma", "__DELETED__"), ("delta", "v1")]

    compacted = compactor.compact([sst_old, sst_new])
    print("Compacted SSTable Level 1:", compacted)
    d = dict(compacted)
    assert d["alpha"] == "v1"
    assert d["beta"] == "v2_updated"
    assert "gamma" not in d # Tombstone purged
    assert d["delta"] == "v1"

    print("LSM-Tree Compactor verified successfully!")

if __name__ == "__main__":
    main()
